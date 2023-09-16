# RB-Colorize

Colorize generates logarithmic color palettes for a given hue. Such an approach prevents the use of opacity and reduces development issues. It supports dark mode and calculates text color for each background color.

This implementation generates CSS/SCSS code and a preview page for layered UI.

I have built an API and a demo stand where you can see how it works: [rockbee.com/colorize](https://rockbee.com/colorize)

## Idea: why logarithmic scale for a palette?

I decided to apply a log scale to 100% lightness and wrote an algorithm that calculates ligtness value for a given number of steps (how many swatches we want to have in our palette; spoiler: 12 is more than enough).

Since a step between each layer is relatively subtle, they can be combined for more nuanced situations.

I call them layers instead of swatches or tones, because it doesn't matter which color they are, they can be used for a layered intefaces.

## Next steps

I want to update this thing one day:

- Build a public API
- Build a Figma plugin
- Build a better demo stand (generate palettes for a given hue instead of random, return readable tokens + JSON copy-paste)

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
