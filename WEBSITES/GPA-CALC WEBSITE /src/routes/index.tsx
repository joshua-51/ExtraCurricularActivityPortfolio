import { createFileRoute } from "@tanstack/react-router";
import { useServerFn } from "@tanstack/react-start";
import { useCallback, useMemo, useRef, useState } from "react";
import { Upload, Loader2, GraduationCap, Trash2, Plus, Sparkles, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { toast } from "sonner";
import { Toaster } from "@/components/ui/sonner";
import { extractGradesFromImage } from "@/lib/gpa.functions";
import { computeGPA, courseAverageBase, type Course, type Level } from "@/lib/gpa";

export const Route = createFileRoute("/")({
  component: Index,
  head: () => ({
    meta: [
      { title: "GPA Calculator — Snap a screenshot, get your GPA" },
      {
        name: "description",
        content:
          "Upload a screenshot of your grades to instantly calculate your weighted or unweighted GPA across any number of marking periods.",
      },
    ],
  }),
});

const GRADE_OPTIONS = ["", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"];

function uid() {
  return Math.random().toString(36).slice(2, 10);
}

function Index() {
  const extract = useServerFn(extractGradesFromImage);
  const fileRef = useRef<HTMLInputElement>(null);
  const [loading, setLoading] = useState(false);
  const [weighted, setWeighted] = useState(false);
  const [mpCount, setMpCount] = useState(4);
  const [courses, setCourses] = useState<Course[]>([]);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);

  const result = useMemo(() => computeGPA(courses, weighted), [courses, weighted]);

  const handleFile = useCallback(
    async (file: File) => {
      if (!file.type.startsWith("image/")) {
        toast.error("Please upload an image file.");
        return;
      }
      setLoading(true);
      const reader = new FileReader();
      reader.onload = async () => {
        const dataUrl = reader.result as string;
        setPreviewUrl(dataUrl);
        try {
          const r = await extract({ data: { imageDataUrl: dataUrl } });
          if (r.error) {
            toast.error(r.error);
          } else if (r.courses.length === 0) {
            toast.error("Couldn't find any grades. Try a clearer screenshot.");
          } else {
            setMpCount(r.markingPeriods);
            setCourses(
              r.courses.map((c) => ({
                id: uid(),
                name: c.name,
                grades: c.grades,
                credits: c.credits,
                level: c.level,
              })),
            );
            toast.success(`Found ${r.courses.length} course${r.courses.length > 1 ? "s" : ""}.`);
          }
        } catch (e) {
          console.error(e);
          toast.error("Something went wrong while analyzing the image.");
        } finally {
          setLoading(false);
        }
      };
      reader.readAsDataURL(file);
    },
    [extract],
  );

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const f = e.dataTransfer.files?.[0];
    if (f) handleFile(f);
  };

  const updateCourse = (id: string, patch: Partial<Course>) =>
    setCourses((cs) => cs.map((c) => (c.id === id ? { ...c, ...patch } : c)));

  const updateMpGrade = (id: string, mpIdx: number, value: string) =>
    setCourses((cs) =>
      cs.map((c) => {
        if (c.id !== id) return c;
        const grades = [...c.grades];
        while (grades.length < mpCount) grades.push("");
        grades[mpIdx] = value;
        return { ...c, grades };
      }),
    );

  const removeCourse = (id: string) => setCourses((cs) => cs.filter((c) => c.id !== id));

  const addCourse = () =>
    setCourses((cs) => [
      ...cs,
      {
        id: uid(),
        name: "New course",
        grades: Array(mpCount).fill(""),
        credits: 1,
        level: "regular",
      },
    ]);

  const addMarkingPeriod = () => {
    setMpCount((n) => n + 1);
    setCourses((cs) => cs.map((c) => ({ ...c, grades: [...c.grades, ""] })));
  };

  const removeMarkingPeriod = (idx: number) => {
    if (mpCount <= 1) return;
    setMpCount((n) => n - 1);
    setCourses((cs) =>
      cs.map((c) => ({
        ...c,
        grades: c.grades.filter((_, i) => i !== idx),
      })),
    );
  };

  const mpIndices = Array.from({ length: mpCount }, (_, i) => i);

  return (
    <div className="min-h-screen bg-gradient-hero">
      <Toaster richColors position="top-center" />
      <main className="mx-auto max-w-6xl px-4 py-12 md:py-20">
        <header className="mb-10 text-center">
          <div className="inline-flex items-center gap-2 rounded-full border border-border bg-card/60 px-3 py-1 text-xs text-muted-foreground backdrop-blur">
            <Sparkles className="h-3.5 w-3.5" /> AI-powered grade extraction
          </div>
          <h1 className="mt-4 text-4xl font-semibold tracking-tight md:text-6xl">
            Snap your grades. <span className="text-gradient">Get your GPA.</span>
          </h1>
          <p className="mx-auto mt-4 max-w-xl text-base text-muted-foreground md:text-lg">
            Upload a screenshot of your transcript and we'll average your marking periods to compute your weighted or unweighted GPA.
          </p>
        </header>

        {courses.length === 0 ? (
          <Card
            className="relative overflow-hidden border-dashed bg-card/50 p-0 shadow-elegant backdrop-blur"
            onDragOver={(e) => e.preventDefault()}
            onDrop={onDrop}
          >
            <button
              type="button"
              onClick={() => fileRef.current?.click()}
              className="flex min-h-[280px] w-full flex-col items-center justify-center gap-4 px-6 py-12 text-center transition-colors hover:bg-accent/40"
              disabled={loading}
            >
              {loading ? (
                <>
                  <Loader2 className="h-10 w-10 animate-spin text-primary" />
                  <div>
                    <p className="text-lg font-medium">Reading your grades…</p>
                    <p className="text-sm text-muted-foreground">This usually takes a few seconds.</p>
                  </div>
                </>
              ) : (
                <>
                  <div className="grid h-14 w-14 place-items-center rounded-full bg-primary/10 text-primary">
                    <Upload className="h-6 w-6" />
                  </div>
                  <div>
                    <p className="text-lg font-medium">Drop a screenshot or click to upload</p>
                    <p className="text-sm text-muted-foreground">PNG, JPG, or HEIC of your transcript or grade report</p>
                  </div>
                </>
              )}
            </button>
            <input
              ref={fileRef}
              type="file"
              accept="image/*"
              className="hidden"
              onChange={(e) => {
                const f = e.target.files?.[0];
                if (f) handleFile(f);
                e.target.value = "";
              }}
            />
          </Card>
        ) : (
          <div className="grid gap-6 lg:grid-cols-[1fr_320px]">
            <Card className="bg-card/70 p-4 shadow-elegant backdrop-blur md:p-6">
              <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
                <h2 className="text-lg font-semibold">Your courses</h2>
                <div className="flex flex-wrap gap-2">
                  <Button variant="outline" size="sm" onClick={addMarkingPeriod}>
                    <Plus className="h-4 w-4" /> Marking period
                  </Button>
                  <Button variant="outline" size="sm" onClick={addCourse}>
                    <Plus className="h-4 w-4" /> Course
                  </Button>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => {
                      setCourses([]);
                      setPreviewUrl(null);
                    }}
                  >
                    Reset
                  </Button>
                </div>
              </div>

              <div className="overflow-x-auto">
                <table className="w-full min-w-[720px] border-separate border-spacing-y-1 text-sm">
                  <thead>
                    <tr className="text-xs uppercase tracking-wide text-muted-foreground">
                      <th className="px-2 text-left font-medium">Course</th>
                      {mpIndices.map((i) => (
                        <th key={i} className="px-1 text-left font-medium">
                          <div className="flex items-center gap-1">
                            <span>MP{i + 1}</span>
                            {mpCount > 1 && (
                              <button
                                type="button"
                                onClick={() => removeMarkingPeriod(i)}
                                className="rounded p-0.5 text-muted-foreground hover:bg-destructive/20 hover:text-destructive"
                                aria-label={`Remove MP${i + 1}`}
                              >
                                <X className="h-3 w-3" />
                              </button>
                            )}
                          </div>
                        </th>
                      ))}
                      <th className="px-2 text-left font-medium">Avg</th>
                      <th className="px-2 text-left font-medium">Credits</th>
                      <th className="px-2 text-left font-medium">Level</th>
                      <th />
                    </tr>
                  </thead>
                  <tbody>
                    {courses.map((c) => {
                      const avg = courseAverageBase(c);
                      return (
                        <tr key={c.id} className="rounded-lg">
                          <td className="bg-background/40 p-1 first:rounded-l-lg">
                            <Input
                              className="min-w-[140px]"
                              value={c.name}
                              onChange={(e) => updateCourse(c.id, { name: e.target.value })}
                              placeholder="Course name"
                            />
                          </td>
                          {mpIndices.map((i) => {
                            const g = c.grades[i] ?? "";
                            return (
                              <td key={i} className="bg-background/40 p-1">
                                <Select
                                  value={g}
                                  onValueChange={(v) => updateMpGrade(c.id, i, v === "—" ? "" : v)}
                                >
                                  <SelectTrigger className="w-[78px]">
                                    <SelectValue placeholder="—" />
                                  </SelectTrigger>
                                  <SelectContent>
                                    {GRADE_OPTIONS.map((opt) => (
                                      <SelectItem key={opt || "blank"} value={opt || "—"}>
                                        {opt || "—"}
                                      </SelectItem>
                                    ))}
                                  </SelectContent>
                                </Select>
                              </td>
                            );
                          })}
                          <td className="bg-background/40 p-1 text-center font-medium tabular-nums">
                            {avg !== null ? avg.toFixed(2) : "—"}
                          </td>
                          <td className="bg-background/40 p-1">
                            <Input
                              type="number"
                              min={0}
                              step={0.5}
                              className="w-[72px]"
                              value={c.credits}
                              onChange={(e) => updateCourse(c.id, { credits: parseFloat(e.target.value) || 0 })}
                            />
                          </td>
                          <td className="bg-background/40 p-1">
                            <Select
                              value={c.level}
                              onValueChange={(v: Level) => updateCourse(c.id, { level: v })}
                            >
                              <SelectTrigger className="w-[150px]">
                                <SelectValue />
                              </SelectTrigger>
                              <SelectContent>
                                <SelectItem value="regular">Regular</SelectItem>
                                <SelectItem value="accelerated">Accelerated (+1.0)</SelectItem>
                                <SelectItem value="honors">Honors / AP (+2.0)</SelectItem>
                              </SelectContent>
                            </Select>
                          </td>
                          <td className="bg-background/40 p-1 last:rounded-r-lg">
                            <Button
                              variant="ghost"
                              size="icon"
                              onClick={() => removeCourse(c.id)}
                              aria-label="Remove course"
                            >
                              <Trash2 className="h-4 w-4" />
                            </Button>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
              <p className="mt-3 text-xs text-muted-foreground">
                Each course's marking-period grades are averaged, then weighted (if enabled) and credit-weighted into the GPA.
              </p>
            </Card>

            <div className="space-y-4">
              <Card className="bg-gradient-card p-6 text-center shadow-elegant">
                <div className="mb-2 flex items-center justify-center gap-2 text-sm text-muted-foreground">
                  <GraduationCap className="h-4 w-4" />
                  {weighted ? "Weighted GPA" : "Unweighted GPA"}
                </div>
                <div className="text-6xl font-semibold tracking-tight text-gradient">
                  {result.gpa.toFixed(2)}
                </div>
                <div className="mt-2 text-xs text-muted-foreground">
                  {result.totalCredits} credit{result.totalCredits === 1 ? "" : "s"} counted
                </div>

                <div className="mt-6 flex items-center justify-between rounded-lg border border-border bg-background/50 px-3 py-2">
                  <Label htmlFor="weighted" className="text-sm">
                    Weighted scale
                  </Label>
                  <Switch id="weighted" checked={weighted} onCheckedChange={setWeighted} />
                </div>
              </Card>

              {previewUrl && (
                <Card className="overflow-hidden p-2">
                  <p className="px-2 py-1 text-xs text-muted-foreground">Source screenshot</p>
                  <img src={previewUrl} alt="Uploaded grades" className="w-full rounded-md" />
                </Card>
              )}

              <Button
                variant="outline"
                className="w-full"
                onClick={() => fileRef.current?.click()}
                disabled={loading}
              >
                <Upload className="h-4 w-4" /> Upload another screenshot
              </Button>
              <input
                ref={fileRef}
                type="file"
                accept="image/*"
                className="hidden"
                onChange={(e) => {
                  const f = e.target.files?.[0];
                  if (f) handleFile(f);
                  e.target.value = "";
                }}
              />
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
