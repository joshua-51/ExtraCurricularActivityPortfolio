export type Level = "regular" | "accelerated" | "honors";

export const GRADE_TO_POINTS: Record<string, number> = {
  "A+": 4.33,
  A: 4.0,
  "A-": 3.67,
  "B+": 3.33,
  B: 3.0,
  "B-": 2.67,
  "C+": 2.33,
  C: 2.0,
  "C-": 1.67,
  D: 1.0,
  F: 0.0,
};

export function gradeToPoints(grade: string): number | null {
  const g = grade.toUpperCase().trim();
  if (g === "") return null;
  if (g in GRADE_TO_POINTS) return GRADE_TO_POINTS[g];
  const num = parseFloat(g);
  if (!isNaN(num)) {
    if (num >= 97) return 4.33;
    if (num >= 93) return 4.0;
    if (num >= 90) return 3.67;
    if (num >= 87) return 3.33;
    if (num >= 83) return 3.0;
    if (num >= 80) return 2.67;
    if (num >= 77) return 2.33;
    if (num >= 73) return 2.0;
    if (num >= 70) return 1.67;
    if (num >= 60) return 1.0;
    return 0;
  }
  return null;
}

// Boost added to the averaged base points for a course.
// D and F (base ≤ 1.0) do not receive a boost.
export function levelBoost(level: Level, basePoints: number): number {
  if (basePoints <= 1.0) return 0;
  if (level === "honors") return 2.0;
  if (level === "accelerated") return 1.0;
  return 0;
}

export type Course = {
  id: string;
  name: string;
  grades: string[]; // one entry per marking period (may be empty string)
  credits: number;
  level: Level;
};

// Average the base points across all non-empty marking periods for a course.
export function courseAverageBase(course: Course): number | null {
  let sum = 0;
  let count = 0;
  for (const g of course.grades) {
    const p = gradeToPoints(g);
    if (p === null) continue;
    sum += p;
    count += 1;
  }
  if (count === 0) return null;
  return sum / count;
}

export function computeGPA(courses: Course[], weighted: boolean) {
  let totalPoints = 0;
  let totalCredits = 0;
  for (const c of courses) {
    const base = courseAverageBase(c);
    if (base === null || c.credits <= 0) continue;
    const pts = base + (weighted ? levelBoost(c.level, base) : 0);
    totalPoints += pts * c.credits;
    totalCredits += c.credits;
  }
  if (totalCredits === 0) return { gpa: 0, totalCredits: 0 };
  return { gpa: totalPoints / totalCredits, totalCredits };
}
