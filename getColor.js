function getColor(h, level, s=90) {

    // Lightness scales for light and dark modes
    const SCALE_LIGHT = [98, 96, 94, 90, 86, 81, 74, 66, 55, 39]
    const SCALE_DARK = [4, 6, 8, 12, 16, 21, 28, 36, 47, 63]

    // Desaturate color for dark mode
    const DARK_DESATURATE = 10

    // TODO: check if saturation is less then DARK_DESATURATE and if so, don't desaturate?

    // Check if level is within range 1-10
    if (level > 10) {level = 10}
    else if (level < 1) {level = 2}

    // TODO: return absolute color -- hsl(hue, 100%, 50%) -- if level > 10

    // Check if hue is within range 0-360:
    if (h < 0 || h > 360) {h = h % 360}

    // prepare HSL colors:
    const light = `hsl: (${h}, ${s}%, ${SCALE_LIGHT[level-1]}%)`
    const dark = `hsl: (${h}, ${s-DARK_DESATURATE}%, ${SCALE_DARK[level-1]}%)`

    return [light, dark]

}

// console.log(getColor(361,11))
// > [ 'hsl: (1, 90%, 39%)', 'hsl: (1, 80%, 63%)' ]