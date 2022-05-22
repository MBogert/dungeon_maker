// const path = require('path')
// const fs = require('fs')
// // Go into that directory, make a list of 2d arrays, and then return said list as a var
// // To pass into the
// // TODO Figure out a solution to run code along with webapp
// function load_dungeons() {
//     let resolved = path.resolve(__dirname, './data/')
//     console.log('resolved: ')
//     console.log(resolved)
//     let dungeons = []
//     fs.readdir(resolved, function (err, files) {
//       if(err){
//         return console.log(err)
//       }
//
//       files.forEach(function (file) {
//         console.log(file)
//         fs.readFile('data/' + file, (err, data) => {
//           if(err) {
//             console.log(err)
//           }
//           console.log(data.toString())
//         })
//       })
//     })
// }
