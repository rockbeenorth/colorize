# RB-Colorize

Compact library to generate CSS/SCSS code and preview for layered UI.

## Idea

Generate color palettes for a UI:

- Core/brand color
- Two additional color palettes
- Errors
- Notifications
- Grayscale

Script generates all libraries based on one hue/saturation pair (only hue required to operate correctly).

## Requirements

Python 3.7 and higher (using a lot of f-strings).

## Install locally

1. Switch to a project folder `cd colorize`.
1. Create a virtual environment `python3 -m venv env`.
1. Activate a virtual environment `source env/bin/activate`
1. `pip install -e .`
1. `python`
1. `import rb_colorize`
2. `rb_colorize.version`

## People suggest reading these

1. https://learnui.design/blog/color-in-ui-design-a-practical-framework.html
2. https://github.com/skratchdot/color-blind
3. https://gka.github.io/chroma.js/
4. https://bottosson.github.io/posts/oklab/
5. https://oklch.evilmartians.io/