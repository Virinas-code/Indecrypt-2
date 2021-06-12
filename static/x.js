let xMenuElement = document.createElement("x-menu-element");
let xInputFile = document.createElement("x-input-file");
let iframe = document.getElementsByTagName("iframe")[0]
let clicks = [];
for (let range = 0 ; range < document.getElementsByTagName("x-menu-element").length ; range++) {
    let element = document.getElementsByTagName("x-menu-element")[range];
    clicks[range] = document.createElement("a");
    clicks[range].appendChild(document.createTextNode(element.getAttribute("href")));
    clicks[range].href = element.getAttribute("href");
    clicks[range].hidden = true;
    document.body.appendChild(clicks[range]);
    element.setAttribute("onclick", "clicks[" + range + "].click();")
}
for (let range = 0 ; range < document.getElementsByTagName("x-input-file").length ; range++) {
    let element = document.getElementsByTagName("x-input-file")[range];
    element.outerHTML = "<form action='' method='POST'><label for='file' class='x-input-file-label'><input type='file' name='file' id='file' class='x-input-file-id-" + range + "' />Select file</label><x-input-file-section><x-input-file-show id='x-input-file-show-" + range + "'></x-input-file-show><input type='submit' value='✓' hidden /></x-input-file-section></form>";
    let result = document.getElementsByClassName("x-input-file-id-" + range)[0];
    let show = document.getElementById("x-input-file-show-" + range);
    console.debug(show);
    result.onchange = function() {
        show.innerHTML = this.value;
        $("x-input-file-section input").show();
    }
}