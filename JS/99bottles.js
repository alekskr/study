var word = "bottles";

var count = 99;

while (count > 0) {
    console.log(count + " " + word + " of beer on the wall");
    console.log(count + " " + word + " of beer,");
    console.log("Take one down, pass it around,");
    document.write(count + " " + word + " of beer on the wall<br>");
    document.write(count + " " + word + " of beer,<br>");
    document.write("Take one down, pass it around,<br>");
    count = count - 1;
    if (count == 1) {
        var word = "bottle";
    }
    if (count > 0) {
        console.log(count + " " + word + " of beer on the wall.");
        document.write(count + " " + word + " of beer on the wall.<br>");
    } else {
        console.log("No more" + word + " of beer on the wall.");
        document.write("No more" + word + " of beer on the wall.<br>");
    }
}
