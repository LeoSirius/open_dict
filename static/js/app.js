function handleSearch(value) {
    console.log(value);
    API.searchWords(value).then(res => {
        console.log(res.data);
    });
}