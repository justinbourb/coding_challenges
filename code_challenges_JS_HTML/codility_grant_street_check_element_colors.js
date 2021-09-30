/*
<!-- HTML example code -->
<table>
        <tbody>
            <tr>
                <td style="color: #ff00ff; background-color:#FFFFFF">Q</td>
            </tr>
        </tbody>
    </table>


 */


// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution() {
    // write your code in Javascript
    //
    // you can access DOM Tree using DOM Object Model:
    //    document.getElementsByTagName
    // or using jQuery:
    //    $('some_tag')
    //
    // please note that element.innerText is not supported,
    // you can use element.textContent instead.
    let td_elements = document.getElementsByTagName('td');
    let results = ''
    for (let i=0; i<td_elements.length; i++){
        if (td_elements[i].style.color != td_elements[i].style.backgroundColor){
            results += td_elements[i].textContent
        }

    }
    return results
}