
function handleAddWord(word_id) {
    API.addWord(word_id).then(res => {
        console.log('add word success');
    })
}

function handleSearch(value) {
    console.log(value);
    let res = '';

    API.searchWords(value).then(res => {
        let display_str = JSON.stringify(res.data);
        let searchResultDiv = document.getElementById('word-meaning');
        let addWordButton = document.getElementById('word-add-button');

        searchResultDiv.innerHTML = display_str;

    function addWord() {
        handleAddWord(res.data.word.word_id)
    }

        console.log('res.data  = ')
        console.log(res.data);
        console.log(res.data.word.word_id);
        addWordButton.style.display = 'block';
        addWordButton.removeEventListener('click', addWord);
        addWordButton.addEventListener('click', addWord);
    });

}