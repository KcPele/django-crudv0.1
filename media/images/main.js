window.onload=getExif;


async function getExif() {
    var img1 = document.getElementById("img1");
    
    EXIF.getData(img1, function() {
        let result = {}
        tags = EXIF.Tags
        for (const [key, value] of Object.entries(tags)) {
            let data = EXIF.getTag(this, value)
            if(data != undefined){
               
               console.log({[value]: data})
            }
          }
    });
    
}