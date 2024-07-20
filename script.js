function validateForm() {
    var name = document.getElementById('name').value;
    var dob = document.getElementById('dob').value;
    var dod = document.getElementById('dod').value;
    var content = document.getElementById('content').value;
    var author = document.getElementById('author').value;

    if (name.trim() === '' || dob.trim() === '' || dod.trim() === '' || content.trim() === '' || author.trim() === '') {
        alert('All fields must be filled out');
        return false;
    }

    return true;
}
