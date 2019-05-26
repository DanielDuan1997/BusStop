const letter = 'p'

let fs = require('fs')

const TextToSVG = require('text-to-svg');
const textToSVG = TextToSVG.loadSync('./barking-cat.otf');

const attributes = {fill: '#4db6ac', stroke: '#00695c'};
const options = {x: 219, y: 0, fontSize: 72, anchor: 'top', attributes: attributes};

const svg = textToSVG.getSVG(letter, options);

fs.writeFile('./' + letter + '.svg', svg, function (err) {
  if (err) {
    throw err;
  }
})