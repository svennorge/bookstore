let myLoad;

let mySave;
mySave = {
    "Id": null,
    "fstname": null,
    "lstname": null,
    "adress1": null,
    "adress2": null,
    "postcode": null,
    "city": null,
    "phone": null,
    "email": null,
    "Communication": {
        "Mobile": null,
        "Home": null
    }};

function download(content, fileName, contentType) {
    var a = document.createElement("a");
    var file = new Blob([content], {type: contentType});
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
}

function saveAsFile() {
    // download(JSON.stringify(mySave), 'json.txt', 'text/plain');
    download(JSON.stringify(mySave), 'Contact.json', 'application/json');
}

function SaveLocal() {

    mySave.fstname = document.getElementById("fstname").value;
    mySave.lstname = document.getElementById("lstname").value;
    mySave.adress1 = document.getElementById("adress1").value;
    mySave.adress2 = document.getElementById("adress2").value;
    mySave.postcode = document.getElementById("postcode").value;
    mySave.city = document.getElementById("city").value;
    mySave.email = document.getElementById("email").value;
    mySave.phone = document.getElementById("phone").value;
    localStorage.setItem("Contact.json", JSON.stringify(mySave));
    download(JSON.stringify(mySave), 'Contact.json', 'application/json');
}


function LoadLocal() {

    myLoad = JSON.parse(localStorage.getItem("Contact.json"));
    document.getElementById("fstname").value = myLoad.fstname;
    document.getElementById("lstname").value = myLoad.lstname;
    document.getElementById("adress1").value = myLoad.adress1;
    document.getElementById("adress2").value = myLoad.adress2;
    document.getElementById("postcode").value = myLoad.postcode;
    document.getElementById("city").value = myLoad.city;
    document.getElementById("email").value = myLoad.email;
    document.getElementById("phone").value = myLoad.phone;

}

function Reset() {
    document.getElementById("fstname").value = null;
    document.getElementById("lstname").value = null;
    document.getElementById("adress1").value = null;
    document.getElementById("adress2").value = null;
    document.getElementById("postcode").value = null;
    document.getElementById("city").value = null;
    document.getElementById("email").value = null;
    document.getElementById("phone").value = null;
}


function saveTraining() {
    let myTraining;
    localStorage.setItem("Training", JSON.stringify(myTraining));
}

function LoadTraining(){
    let myTraining;
    myTraining = JSON.parse(localStorage.getItem("Training"));
}
