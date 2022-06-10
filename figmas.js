
// expected hue range: [0, 360)
// expected saturation range: [0, 1]
// expected lightness range: [0, 1]
var hslToRgb = function (hue, saturation, lightness) {
    // based on algorithm from http://en.wikipedia.org/wiki/HSL_and_HSV#Converting_to_RGB
    if (hue == undefined) {
        return [0, 0, 0];
    }

    var chroma = (1 - Math.abs((2 * lightness) - 1)) * saturation;
    var huePrime = hue / 60;
    var secondComponent = chroma * (1 - Math.abs((huePrime % 2) - 1));

    huePrime = Math.floor(huePrime);
    var red;
    var green;
    var blue;

    if (huePrime === 0) {
        red = chroma;
        green = secondComponent;
        blue = 0;
    } else if (huePrime === 1) {
        red = secondComponent;
        green = chroma;
        blue = 0;
    } else if (huePrime === 2) {
        red = 0;
        green = chroma;
        blue = secondComponent;
    } else if (huePrime === 3) {
        red = 0;
        green = secondComponent;
        blue = chroma;
    } else if (huePrime === 4) {
        red = secondComponent;
        green = 0;
        blue = chroma;
    } else if (huePrime === 5) {
        red = chroma;
        green = 0;
        blue = secondComponent;
    }

    var lightnessAdjustment = lightness - (chroma / 2);
    red += lightnessAdjustment;
    green += lightnessAdjustment;
    blue += lightnessAdjustment;

    //   return [Math.round(red * 255), Math.round(green * 255), Math.round(blue * 255)];
    return {
        r: Math.round(red * 255),
        g: Math.round(green * 255),
        b: Math.round(blue * 255)
    };

};


function getColor(h, level = 0, s = 90) {

    if (!Number.isInteger(h) || !Number.isInteger(level) || !Number.isInteger(s)) {
        throw 'All parameters should be numbers (integers).';
    }

    if (level < 0 || level > 10) {
        throw `The level argument should be between 0 and 10, but ${level} was given instead.`
    };
    const SCALE_LIGHT = [98, 96, 94, 90, 86, 81, 74, 66, 55, 39];
    const SCALE_DARK = [4, 6, 8, 12, 16, 21, 28, 36, 47, 63];

    const DARK_DESATURATE = 10;

    let darkDesaturate;
    if (s <= DARK_DESATURATE) {
        darkDesaturate = 0;
    } else { darkDesaturate = DARK_DESATURATE; }

    if (h > 360) { h = h % 360 };
    if (h < 0) {
        h = 360 - (Math.abs(h) % 360);
    };

    if (level == 0) {
        return [
            `hsl(${h}, 100%, 50%)`,
            `hsl(${h}, ${100 - darkDesaturate}%, 50%)`
        ]
    };

    // const light = `hsl(${h}, ${s}%, ${SCALE_LIGHT[level - 1]}%)`;
    // const dark = `hsl(${h}, ${s - darkDesaturate}%, ${SCALE_DARK[level - 1]}%)`;

    const [lR, lG, lB] = [h, s / 100, (SCALE_LIGHT[level - 1]) / 100]
    const [dR, dG, dB] = [h, (s - darkDesaturate) / 100, (SCALE_DARK[level - 1]) / 100]

    const light = {
        name: `light/${h}-${level}`,
        rgb: hslToRgb(lR, lG, lB)
    }
    const dark =
    {
        name: `dark/${h}-${level}`,
        rgb: hslToRgb(dR, dG, dB)
    }




    return [light, dark]

}


console.log(getColor(17, 2))


// function createShapes(colors) {

//     let xPos = 80
//     let yPos = 80
//     let count = 0

//     let objects = []

//     for (let colorObject of colors) { // Do for every color

//         // Circle
//         let circle: EllipseNode = figma.createEllipse()
//         circle.resize(60, 60)
//         circle.x = xPos + (circle.width * count)
//         circle.y = yPos
//         xPos += 20

//         let color: RGB = hexToRgbRange(colorObject.hex)
//         circle.fills = [{ type: 'SOLID', color: color }]
//         circle.name = colorObject.name

//         const style = figma.createPaintStyle()
//         style.name = colorObject.name
//         style.paints = [{ type: 'SOLID', color: color }]

//         //currentPage.appendChild(circle)


//         objects.push(circle)

//         count += 1
//     }

//     figma.currentPage.selection = objects
//     figma.viewport.scrollAndZoomIntoView(objects)

// }




function hexToRgbRange(hex) {
//  let defaultColor:RGB = {r: 255, g: 255, b:255} // in case of error
 let defaultColor = {r: 255, g: 255, b:255} // in case of error
  let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex)
  return result ? {
    r: parseInt(result[1], 16) / 255,
    g: parseInt(result[2], 16) / 255,
    b: parseInt(result[3], 16) / 255
  } : defaultColor
}


console.log(hexToRgbRange())



// function createShapes(colors: Array<any>) {

//     let xPos = 80
//     let yPos = 80
//     let count = 0

//     let objects: Array<any> = []

//     for (let colorObject of colors) { // Do for every color

//         // Circle
//         let circle: EllipseNode = figma.createEllipse()
//         circle.resize(60, 60)
//         circle.x = xPos + (circle.width * count)
//         circle.y = yPos
//         xPos += 20

//         let color: RGB = colorObject.rgb
//         circle.fills = [{ type: 'SOLID', color: color }]
//         circle.name = colorObject.name

//         const style = figma.createPaintStyle()
//         style.name = colorObject.name
//         style.paints = [{ type: 'SOLID', color: color }]

//         // currentPage.appendChild(circle)


//         objects.push(circle)

//         count += 1
//     }

//     figma.currentPage.selection = objects
//     figma.viewport.scrollAndZoomIntoView(objects)
// }
