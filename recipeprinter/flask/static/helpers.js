let id_counter = 1;

function printDiv(divId) {
    var printContents = document.getElementById(divId).innerHTML;
    var originalContents = document.body.innerHTML;

    document.body.innerHTML = printContents;

    window.print();
    
    document.body.innerHTML = originalContents;
  }


function delete_row(id){
    document.getElementById(id).remove();
}

function create_new_ingredient_row(){
    
    let my_form = document.getElementById('create-recipe-form-content');
    let node = my_form.firstElementChild.cloneNode(true);

    // remove old text and space filler
    node.getElementsByClassName('ingr-text-input')[0].value = '';
    node.getElementsByClassName('space-filler')[0].remove();

    // add id to inputs
    let id = id_counter++;
    node.getElementsByClassName('ingr-text-input')[0].name = id + ':name';
    node.getElementsByClassName('ingr-type-input')[0].name = id + ':type';
    node.getElementsByClassName('ingr-unit-input')[0].name = id + ':unit';
    node.getElementsByClassName('ingr-2ppl-input')[0].name = id + ':2ppl';
    node.getElementsByClassName('ingr-4ppl-input')[0].name = id + ':4ppl';

    node.setAttribute('id', id);
    
    // add delete button
    let remove_btn = document.createElement('button');
    remove_btn.setAttribute('onClick', `delete_row('${id}')`);
    remove_btn.innerText = 'x';

    // append to document
    node.appendChild(remove_btn);
    my_form.appendChild(node);
}