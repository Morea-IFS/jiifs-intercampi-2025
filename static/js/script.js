document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.querySelector(".side-bar");
    const invisibleSidebar = document.querySelector(".invisible-side-bar");

    if (!sidebar || !invisibleSidebar) return; // Evita erros se os elementos não existirem

    // Função para atualizar a largura da "invisible-side-bar" e adicionar +1em
    function updateInvisibleSidebar() {
        const sidebarWidth = sidebar.offsetWidth; // Obtém a largura da sidebar
        invisibleSidebar.style.width = `${sidebarWidth - 1}px`; // Aplica a nova largura
    }

    // Executa a função imediatamente
    updateInvisibleSidebar();

    // Atualiza sempre que a janela for redimensionada
    window.addEventListener("resize", updateInvisibleSidebar);

    // Usa MutationObserver para detectar mudanças na sidebar
    const observer = new MutationObserver(updateInvisibleSidebar);
    observer.observe(sidebar, { attributes: true, childList: true, subtree: true });

    // Garante que o script rode mesmo após um F5
    window.addEventListener("load", updateInvisibleSidebar);
});



// Light mode and dark mode Script
const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");
const body = document.body;

// Alterna entre modo claro e escuro
function toggleTheme() {
    const isLightMode = body.classList.contains("light-mode");

    if (isLightMode) {
        body.classList.remove("light-mode");
        body.classList.add("dark-mode");
        themeIcon.classList.remove("fa-sun");
        themeIcon.classList.add("fa-moon");
        localStorage.setItem("theme", "dark");
    } else {
        body.classList.remove("dark-mode");
        body.classList.add("light-mode");
        themeIcon.classList.remove("fa-moon");
        themeIcon.classList.add("fa-sun");
        localStorage.setItem("theme", "light-mode");
    }

    console.log(`Modo ${isLightMode ? "escuro" : "claro"} ativado`);
}

// Aplica o tema salvo no localStorage ou usa escuro por padrão
function loadTheme() {
    const storedTheme = localStorage.getItem("theme");

    if (storedTheme === "light-mode") {
        body.classList.add("light-mode");
        themeIcon.classList.add("fa-sun");
    } else {
        body.classList.add("dark-mode");
        themeIcon.classList.add("fa-moon");
    }
}

// Carrega o tema ao iniciar
loadTheme();

// Evento de clique para alternar
themeToggle.addEventListener("click", toggleTheme);



function trocarTextoLabel() {
    const label = document.getElementById("label-foto");
    const input = document.getElementById("fotos");

    // Se um arquivo for selecionado, muda o texto do label
    if (input.files.length > 0) {
        label.innerHTML = "Imagem anexada";
    } else {
        // Se nenhum arquivo estiver selecionado, volta para o texto padrão
        label.innerHTML = "Adicione uma imagem";
    }
}

function trocarTextoBELabel() {
    const label = document.getElementById("label-bulletin");
    const input = document.getElementById("bulletin");

    // Se um arquivo for selecionado, muda o texto do label
    if (input.files.length > 0) {
        label.innerHTML = "Boletim escolar anexado";
    } else {
        // Se nenhum arquivo estiver selecionado, volta para o texto padrão
        label.innerHTML = "Clique aqui e adicione o boletim escolar";
    }
}

function trocarTextoRGLabel() {
    const label = document.getElementById("label-general-register");
    const input = document.getElementById("general-register");

    // Se um arquivo for selecionado, muda o texto do label
    if (input.files.length > 0) {
        label.innerHTML = "RG anexado";
    } else {
        // Se nenhum arquivo estiver selecionado, volta para o texto padrão
        label.innerHTML = "Clique aqui e anexe o rg";
    }
}

function trocarTextoLabelspreadsheetv(){
    const label = document.getElementById("label-spreadsheet");
    const input = document.getElementById("spreadsheet");

    // Se um arquivo for selecionado, muda o texto do label
    if (input.files.length > 0) {
        label.innerHTML = "Planilha selecionada";
    } else {
        // Se nenhum arquivo estiver selecionado, volta para o texto padrão
        label.innerHTML = "Selecione uma planilha";
    }
}

function toggle_checkbox(source) {
    checkboxes = document.getElementsByName("input-checkbox");
    for (i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function search_table() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search-input");
    filter = input.value.toUpperCase();
    table = document.getElementById("search-table");
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {
        // Começa em 1 para pular o cabeçalho
        tr[i].style.display = "none"; // Oculta a linha por padrão
        td = tr[i].getElementsByTagName("td");
        for (var j = 0; j < td.length; j++) {
            if (td[j]) {
                txtValue = td[j].textContent || td[j].innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = ""; // Mostra a linha se houver correspondência
                    break;
                }
            }
        }
    }
}

// Function for mobile hamburger menu.
function toggle(element) {
    element.classList.toggle("change");
}

function exibirAlerta(mensagem) {
    if (mensagem) {
        window.alert(mensagem);
    }
}
function enviar1Formularios() {
    console.log("form1")
    // Obter os dados do primeiro formulário
    const form1 = new FormData(document.getElementById('form1'));
    const form2 = document.getElementById('form2');

    // Adicionar os dados do form1 ao form2
    for (let [key, value] of form1.entries()) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value;
        form2.appendChild(input);
    }

    // Submeter o segundo formulário com os dados combinados
    form2.submit();
}
function enviar2Formularios() {
    console.log("form2")
    // Obter os dados do primeiro formulário
    const form3 = new FormData(document.getElementById('form3'));
    const form4 = document.getElementById('form4');

    // Adicionar os dados do form1 ao form2
    for (let [key, value] of form3.entries()) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value;
        form4.appendChild(input);
    }

    // Submeter o segundo formulário com os dados combinados
    form4.submit();
}
function enviar3Formularios() {
    console.log("form3")
    // Obter os dados do primeiro formulário
    const form1 = new FormData(document.getElementById('form1'));
    const form5 = document.getElementById('form5');

    // Adicionar os dados do form1 ao form2
    for (let [key, value] of form1.entries()) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value;
        form5.appendChild(input);
    }
    console.log(form5, form1)
    // Submeter o segundo formulário com os dados combinados
    form5.submit();
}

function enviar4Formularios() {
    console.log("form2")
    // Obter os dados do primeiro formulário
    const form3 = new FormData(document.getElementById('form3'));
    const form6 = document.getElementById('form6');

    // Adicionar os dados do form1 ao form2
    for (let [key, value] of form3.entries()) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value;
        form6.appendChild(input);
    }

    // Submeter o segundo formulário com os dados combinados
    form6.submit();
}




function mostrarCampos() {
    const tipo = document.getElementById('tipo').value;
    const camposPenalidade = document.getElementById('camposPenalidade');
    const camposAssistencia = document.getElementById('camposAssistencia');
    const camposAcrescimo = document.getElementById('camposAcrescimo');
    const camposSets = document.getElementById('camposSets');
    const camposEnd = document.getElementById('camposEnd');
    const camposWinner = document.getElementById('camposWinner');
    const camposBanner = document.getElementById('camposBanner')

    // Esconder todos os campos inicialmente
    camposPenalidade.classList.add('hidden');
    camposAssistencia.classList.add('hidden');
    camposAcrescimo.classList.add('hidden');
    camposSets.classList.add('hidden');
    camposEnd.classList.add('hidden');
    camposWinner.classList.add('hidden');
    camposBanner.classList.add('hidden');

    // Exibir os campos com base na escolha
    if (tipo === 'penalidade') {
        camposPenalidade.classList.remove('hidden');
    } else if (tipo === 'assistencia') {
        camposAssistencia.classList.remove('hidden');
    }else if (tipo === 'acrescimo') {
        camposAcrescimo.classList.remove('hidden');
    }else if (tipo === 'sets') {
        camposSets.classList.remove('hidden');
    }else if (tipo === 'end') {
        camposEnd.classList.remove('hidden');
    }else if (tipo === 'winner') {
        camposWinner.classList.remove('hidden');
    }else if (tipo === 'banner') {
        camposBanner.classList.remove('hidden');
    }
}

function confirmAction(event, message) {
    if (!message) return;
    
    if (!window.confirm(message) && event) {
        event.preventDefault(); // Cancela a ação se o usuário clicar em "Cancelar"
    }
}

// Mapeia os botões e aplica eventos de confirmação dinamicamente
function applyConfirmation() {
    document.querySelectorAll("[data-confirm]").forEach(button => {
        button.addEventListener("click", event => {
            const message = button.getAttribute("data-confirm");
            confirmAction(event, message);
        });
    });
}

document.addEventListener("DOMContentLoaded", applyConfirmation);
