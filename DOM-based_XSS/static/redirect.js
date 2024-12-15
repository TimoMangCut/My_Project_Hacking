function getURL(name) {
    const URLparams = new URLSearchParams(window.location.search);
    return URLparams.get(name);
}
const Redirect = getURL('url');
if (Redirect) {
    window.location.href = Redirect;
}