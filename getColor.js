function getColor(h, level, s=90) {

    // Lightness scales for light and dark modes
    const SCALE_LIGHT = [98, 96, 94, 90, 86, 81, 74, 66, 55, 39]
    const SCALE_DARK = [4, 6, 8, 12, 16, 21, 28, 36, 47, 63]
    const DARK_DESATURATE = 10

    if (level > 10) {level = 10}
    else if (level < 1) {level = 2}

    if (h < 0 || h > 360) {h = h % 360}

    const light = `hsl: (${h}, ${s}%, ${SCALE_LIGHT[level-1]}%)`
    const dark = `hsl: (${h}, ${s-DARK_DESATURATE}%, ${SCALE_DARK[level-1]}%)`

    return [light, dark]

}

console.log(getColor(12,10))