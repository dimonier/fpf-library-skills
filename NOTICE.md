# Notices

This repository packages the **FPF Library** (First Principles Framework) by Anatoly
Levenchuk as agent skills. It mixes three kinds of material under different rights.
Read this before reusing or redistributing.

## 1. FPF framework text — © Anatoly Levenchuk, CC BY 4.0

The framework text is Anatoly Levenchuk's and is licensed under the
[Creative Commons Attribution 4.0 International license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
This covers, in each content skill (`fpf-core/` and `dpf-*/`):

- `assets/*.md` — the monolith source (`FPF-Spec.md`, the DPF framework files);
- `references/*.md` — the per-pattern decomposition (pattern bodies reproduced verbatim);
- `context/*.md` — reader-help sections extracted from the source.

> Anatoly Levenchuk, First Principles Framework (FPF) and Domain Principle Frameworks,
> FPF Library. https://github.com/ailev/FPF

Copyright (c) Anatoly Levenchuk. Licensed under CC BY 4.0. Provided "as is", without
warranties of any kind.

**Changes:** the monolithic framework publications were decomposed source-faithfully —
one file per pattern plus `INDEX.md` routing — with frontmatter metadata added. Pattern
bodies follow the source verbatim unless a skill's own `NOTICE.md` states otherwise. The
full license text is in [LICENSE](LICENSE) and in each skill's `LICENSE` file.

Attribution must not imply Anatoly Levenchuk endorses this repackaging.

## 2. Packaging, routing and tooling — © Dmitry Ulanov

The skill packaging is original work by Dmitry Ulanov:

- **Routing text** — `SKILL.md` dispatcher text, `description` fields, `references/INDEX.md`,
  this README and NOTICE — licensed under CC BY 4.0 to keep the package reusable on
  uniform terms.
- **Tooling** — `fpf-library-sync/` is entirely original maintenance tooling (it builds
  both `fpf-core` and the `dpf-*` skills), licensed under the MIT License. See
  `fpf-library-sync/LICENSE`.

## 3. Third-party material quoted inside the FPF text

Quotations, citations and imported source literature printed inside the framework text
remain subject to their rights holders' terms. CC BY 4.0 does not relicense them, and a
bibliographic reference does not grant a right to reprint the cited work. Follow the
source credits printed in the published frameworks.