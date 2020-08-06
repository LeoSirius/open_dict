const API = {
    req: axios.create(),
    searchWords: function (words) {
        const url = '/api/search-words/?words=' + words;
        return this.req.get(url);
    }
}