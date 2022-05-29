function getColor(h, level = 0, s = 90) {

    if (!Number.isInteger(h) || !Number.isInteger(level) || !Number.isInteger(s)) {
        throw 'All parameters should be numbers (integers).';
    }

    // Lightness scales for light and dark modes
    const SCALE_LIGHT = [98, 96, 94, 90, 86, 81, 74, 66, 55, 39]
    const SCALE_DARK = [4, 6, 8, 12, 16, 21, 28, 36, 47, 63]

    // Define step to desaturate color for dark mode
    let darkDesaturate = 10

    // If saturation is less then darkDesaturate don't desaturate:

    if (s <= darkDesaturate) {
        darkDesaturate = 0;
    }

    // Normalize the hue to the range 0-360.
    // It is NOT an error, because sometimes you need to calculate 
    // the opposite or additional hue number and it can be out of range 
    // but still remain a valid color.

    if (h > 360) { h = h % 360 }
    if (h < 0) {
        let delta = Math.abs(h) % 360;
        h = 360 - delta;
    }

    // Return the absolute/default color for level 0 -- hsl(hue, 100%, 50%)
    // Level 0 returns absulute color with maxed out saturation and 50%
    // lightness. Dark version gets desaturated by a darkDesaturate step value.

    if (level == 0) {
        return [
            `hsl(${h}, 100%, 50%)`,
            `hsl(${h}, ${100 - darkDesaturate}%, 50%)`
        ]
    }

    // Check if level is within range 1-10

    if (level < 0 || level > 10) {
        throw `The level argument should be between 0 and 10, but ${level} was given instead.`
    }

    // prepare HSL colors:
    const light = `hsl(${h}, ${s}%, ${SCALE_LIGHT[level - 1]}%)`
    const dark = `hsl(${h}, ${s - darkDesaturate}%, ${SCALE_DARK[level - 1]}%)`

    return [light, dark]

}

// console.log(getColor(360, 5))
// > [ 'hsl: (1, 90%, 39%)', 'hsl: (1, 80%, 63%)' ]


console.log(getColor(-17, 7))