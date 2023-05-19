function downloadFile(name) {
    console.log(name);
    fetch("http://localhost:8000/download?name=" + name)
        .then(r => console.log(r));
}