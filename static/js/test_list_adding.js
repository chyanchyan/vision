counter = 1
function add(){
    var x = document.createElement('li');
    x.className = 'list-item';
    x.innerHTML = 'the counter is' + counter;
    document.getElementById('the-list').appendChild(x);
    counter++;
};