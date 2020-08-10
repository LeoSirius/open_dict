

function handleSearch(value) {
    console.log(value);
    let res = ''
    API.searchWords(value).then(res => {
        console.log(res.data);
        res = JSON.stringify(res.data);
        let searchResultDiv = document.getElementById('search-result');
        console.log(searchResultDiv)
        searchResultDiv.innerHTML = res;

    });


}