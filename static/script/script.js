function updateInput(ish){
    antal = 0.5*parseFloat(document.getElementById("børn").value) + parseFloat(document.getElementById("voksne").value);
    enhedspris = parseFloat(document.getElementById("enhedspris").value)
    transport = parseFloat(document.getElementById("transport").value)
    document.getElementById("total").value = (antal * enhedspris + transport).toFixed(2);
    document.getElementById("moms").value = ((antal * enhedspris + transport)*0.20).toFixed(2);

}

function transportInput(val) {
    c = document.getElementById("bekraeft_transport")
    if(c.checked) {
        document.getElementById("transport").value = parseFloat(150.00);
    } else {
        document.getElementById("transport").value = 0;
    }
    updateInput(val)
}
    