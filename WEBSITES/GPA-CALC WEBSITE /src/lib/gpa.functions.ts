import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";

const InputSchema = z.object({
  imageDataUrl: z.string().min(20),
});

export type ExtractedCourse = {
  name: string;
  grades: string[]; // grade per marking period, "" if missing
  credits: number;
  level: "regular" | "accelerated" | "honors";
};

export type ExtractResult = {
  courses: ExtractedCourse[];
  markingPeriods: number;
  error: string | null;
};

export const extractGradesFromImage = createServerFn({ method: "POST" })
  .inputValidator((d) => InputSchema.parse(d))
  .handler(async ({ data }): Promise<ExtractResult> => {
    const apiKey = process.env.LOVABLE_API_KEY;
    if (!apiKey) {
      return { courses: [], markingPeriods: 4, error: "AI gateway not configured." };
    }

    const systemPrompt =
      "You extract a student's courses from a screenshot of a transcript or grade report. Identify the marking-period columns (e.g. MP1, MP2, MP3, MP4, Q1-Q4, T1-T3, S1-S2, etc.) and return one grade per marking period for each course, in order. If a marking period is blank for a course, return an empty string for that slot. Respond ONLY by calling the provided tool. Map difficulty: 'honors' for Honors/AP/IB/H/-H suffix (highest weight); 'accelerated' for Accelerated/Pre-AP/Advanced (mid weight); else 'regular'. If credits aren't visible, use 1. Use letter grades (A+, A, A-, B+, B, B-, C+, C, C-, D, F). Convert numeric: 97-100=A+, 93-96=A, 90-92=A-, 87-89=B+, 83-86=B, 80-82=B-, 77-79=C+, 73-76=C, 70-72=C-, 60-69=D, <60=F. Ignore final-grade or earned columns — only the per-period grades. Ignore satisfaction/comment letters like a single 'S'.";

    try {
      const res = await fetch("https://ai.gateway.lovable.dev/v1/chat/completions", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          model: "google/gemini-2.5-flash",
          messages: [
            { role: "system", content: systemPrompt },
            {
              role: "user",
              content: [
                { type: "text", text: "Extract every course with its per-marking-period grades, credits, and level. Also report how many marking-period columns the report has." },
                { type: "image_url", image_url: { url: data.imageDataUrl } },
              ],
            },
          ],
          tools: [
            {
              type: "function",
              function: {
                name: "submit_courses",
                description: "Submit extracted courses with per-marking-period grades.",
                parameters: {
                  type: "object",
                  properties: {
                    markingPeriods: { type: "number", description: "Number of marking-period columns detected." },
                    courses: {
                      type: "array",
                      items: {
                        type: "object",
                        properties: {
                          name: { type: "string" },
                          grades: {
                            type: "array",
                            items: { type: "string" },
                            description: "One grade per marking period, in order. Empty string if blank.",
                          },
                          credits: { type: "number" },
                          level: { type: "string", enum: ["regular", "accelerated", "honors"] },
                        },
                        required: ["name", "grades", "credits", "level"],
                        additionalProperties: false,
                      },
                    },
                  },
                  required: ["markingPeriods", "courses"],
                  additionalProperties: false,
                },
              },
            },
          ],
          tool_choice: { type: "function", function: { name: "submit_courses" } },
        }),
      });

      if (res.status === 429) return { courses: [], markingPeriods: 4, error: "Rate limit reached. Try again shortly." };
      if (res.status === 402) return { courses: [], markingPeriods: 4, error: "AI credits exhausted. Add credits in Lovable Cloud." };
      if (!res.ok) {
        const t = await res.text();
        console.error("AI gateway error", res.status, t);
        return { courses: [], markingPeriods: 4, error: `AI request failed (${res.status}).` };
      }

      const json = await res.json();
      const call = json?.choices?.[0]?.message?.tool_calls?.[0];
      if (!call) return { courses: [], markingPeriods: 4, error: "No grades detected in the image." };
      const args = JSON.parse(call.function.arguments);
      const mp = Math.max(1, Math.min(12, Number(args.markingPeriods) || 4));
      const courses: ExtractedCourse[] = (args.courses ?? []).map((c: ExtractedCourse) => {
        const grades = Array.isArray(c.grades) ? c.grades.map((g) => String(g ?? "").toUpperCase().trim()) : [];
        while (grades.length < mp) grades.push("");
        grades.length = mp;
        return {
          name: String(c.name ?? ""),
          grades,
          credits: Number(c.credits) || 1,
          level: (c.level === "honors" || c.level === "accelerated" ? c.level : "regular") as ExtractedCourse["level"],
        };
      });
      return { courses, markingPeriods: mp, error: null };
    } catch (e) {
      console.error(e);
      return { courses: [], markingPeriods: 4, error: "Failed to analyze the image." };
    }
  });
