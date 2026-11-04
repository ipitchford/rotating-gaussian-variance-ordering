# Build the manuscript PDF

The authoritative manuscript is [manuscript.md](manuscript.md). The supplied [LaTeX source](output/latex/rotating_gaussian_variance.tex) is generated from it; edit the Markdown when preparing a future revision.

## Requirements

Install Pandoc and a TeX distribution providing `pdflatex`. Version 1.2 was built with Homebrew Pandoc and pdfTeX; script letters render as calligraphic (`\\mathcal`) so the rsfs font is not required. Other compatible versions may produce small layout differences.

The manuscript's YAML header explicitly requires the LaTeX packages `amsmath`, `amssymb`, `mathtools`, `microtype` and `booktabs`. Pandoc's generated header also uses the standard article class, Latin Modern fonts (`lmodern`), `iftex`, `fontenc`, `inputenc`, `textcomp`, `xcolor`, `geometry`, `graphicx`, `babel` with British English support, `etoolbox`, and `hyperref` (directly or through `bookmark`). Its optional package probes include `upquote`, `parskip` and `xurl`. A sufficiently complete TeX Live or MiKTeX installation supplies these dependencies.

The included figure [figures/variance_landscape.pdf](figures/variance_landscape.pdf) must be present. No bibliography processor is needed: the references are written directly in the manuscript.

## Commands

Run the following **with `research_sampling` as the working directory**. Keep that working directory for both LaTeX passes so the relative figure path resolves.

```bash
mkdir -p output/latex output/pdf
pandoc manuscript.md --from=markdown+tex_math_dollars+raw_tex --to=latex --standalone --output=output/latex/rotating_gaussian_variance.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output/pdf output/latex/rotating_gaussian_variance.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output/pdf output/latex/rotating_gaussian_variance.tex
```

The final document is [output/pdf/rotating_gaussian_variance.pdf](output/pdf/rotating_gaussian_variance.pdf). The second LaTeX pass resolves document links and references. The `.log` and auxiliary files are written beside the PDF; inspect the log if a command fails or reports unresolved references. These commands overwrite the generated LaTeX and PDF, while leaving the Markdown source unchanged.

The manuscript SHA-256 is recorded in MANIFEST.sha256 (version 1.2; the publisher updates it after inserting the DOI).

```text
see MANIFEST.sha256
```

## Reproduce the calculations or figure

The Python calculations are separate from the document build. See [code/README.md](code/README.md) for dependencies, both verification scripts, their JSON reports and figure regeneration. With the supplied figure already present, rebuilding the PDF does not require Python or another verification run.
