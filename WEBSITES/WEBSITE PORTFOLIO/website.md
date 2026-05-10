# Website Overview

This page is a personal portfolio website for Joshua Kothapalle. It is a single-page layout built with HTML, internal CSS, and a small JavaScript script to create polished visual interactions.

## Design and Theme

- Uses a dark, modern design with high contrast between rich black backgrounds and bright orange highlights.
- Includes custom fonts from Google Fonts: `Bebas Neue` for display text and `Space Grotesk` for body text.
- Implements a noise overlay, custom cursor, and subtle glow effects to add texture and motion.
- Uses soft animations (`fadeUp`, `fadeIn`, marquee movement, and scroll reveal) to make content appear smoothly.

## Page Structure

1. **Navigation**
   - Fixed nav bar with site branding (`JK.`) and anchor links to page sections.
   - The nav condenses padding when the user scrolls down.

2. **Hero Section**
   - Full-screen introduction featuring Joshua's name, tagline, and CTA buttons.
   - Includes a decorative oversized background letter `J` and a scroll indicator.

3. **Marquee**
   - A horizontal scrolling banner showcasing keywords like `Python`, `Java`, `JavaScript`, `Open Source`, and `Leadership`.
   - Repeats the same content to create a continuous sliding effect.

4. **About**
   - Provides a personal statement about Joshua's interests in computer science, engineering, robotics, and entrepreneurship.
   - Displays achievement stats: CS50 certification, ACSL finalist, open source repos, and an endless drive to build.

5. **Skills**
   - Three skill categories: Languages, Technical, and Leadership & Soft Skills.
   - Each category includes tags for competencies such as Python, Java, Git, UI/UX design, teamwork, and critical thinking.

6. **Achievements**
   - Highlights five accomplishments: ACSL Finalist, Harvard CS50 Python Certificate, Open Source Contributions, Robotics Team membership, and Community Impact.
   - Uses hover effects to reveal accent styling.

7. **Experience**
   - Presents real-world experiences such as open source contributions, local business web development, robotics, marching band, and tennis.
   - A special summary card emphasizes Joshua's strength in both technical ability and communication.

8. **Projects**
   - Features portfolio items linking to the GitHub repository.
   - Includes website, restaurant web design, open source contributions, Python projects, and robotics work.
   - A final card encourages visitors to explore more on GitHub.

9. **Mission**
   - A centered statement about combining technology, creativity, and leadership.
   - Expresses goals around internships, innovative projects, and attending a top university.

10. **Contact**
    - Provides an email contact link with a strong call to connect.
    - Includes a GitHub portfolio CTA and footer links.

## Interactive Features

- **Custom Cursor**: A small orange dot and ring follow the cursor, expanding on hover over interactive elements.
- **Hover State**: Links, buttons, project cards, achievement items, experience cards, and skill blocks trigger a `hovering` state to enlarge the cursor ring.
- **Scroll Reveal**: Elements with `.reveal` fade into view as the user scrolls.
- **Navigation Shrink**: The nav bar padding reduces once the page scrolls past a threshold.
- **Background Parallax**: The large hero background letter moves slightly with scroll to create depth.

## Responsive Behavior

- Adjusts layout for screens below 900px.
- Hides nav links on smaller screens and stacks grid sections vertically.
- Simplifies achievement badges and content spacing for mobile devices.

## Purpose

The page is designed as a polished portfolio landing page for a student developer. It highlights technical skill, achievements, projects, and extracurricular leadership through a strong visual brand and smooth UI interactions.
