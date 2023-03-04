$(function () {
    // POBRANIE PRZYCISKU
    const btnMove = $('#btnMove')

    // POZYSKANIE CSRFTOKENA
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    // FUNKCJA AJAX - POST DO WYSŁANIA DANYCH
    const sendData = function (dataToSend, site) {

        $.post({
            headers: {'X-CSRFToken': csrftoken},
            // contentType: 'application/json',
            url: '/construction/' + site + '/',
            data: dataToSend,
            // dataType: 'json',
        }).done(function () {
            location.reload()
        }).fail(function () {
            alert('Błąd')
        })
    }


    // EVENT NA PRZYCISK
    btnMove.on('click', function () {
        // pobranie id lokalizacji - budowa/magazyn
        const site = $('#site option:selected').val()
        // pobranie zanaczonych narzędzi
        const input = $('input:checked')
        // uwtorzenie słownika z wpisem lokalizacja
        const dataToSend = {'location': site}
        // iteracja po zaznaczonych narzędziach i dodanie ich do słownika
        input.each(function (index, element) {
            dataToSend[index] = element.value
        })
        sendData(dataToSend, site)

    })
})
