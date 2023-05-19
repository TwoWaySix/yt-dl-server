async function test() {
    console.log("Test");

    const baseUrl = "localhost:8000/download?url="
    const downloadUrl = "https://www.youtube.com/watch?v=IBCuZff5Vhk";
    const response = await fetch(baseUrl+downloadUrl, {
        method: "GET", 
    });
    console.log(response.text());
}

