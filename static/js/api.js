const API = {
    req: axios.create(),
    searchWords: function (words) {
        const url = '/api/search-words/?words=' + words;
        return this.req.get(url);
    },

    addWord: function (word_id) {
        const url = '/api/user-words/?word_id=' + word_id;
        return this.req.post(url);
    }
}