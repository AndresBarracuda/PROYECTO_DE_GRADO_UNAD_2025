// CRM UNAD Custom JavaScript

$(document).ready(function() {
    // Configurar headers AJAX para CSRF
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", $('[name=csrfmiddlewaretoken]').val());
            }
        }
    });

    // Prevenir cache del navegador para páginas protegidas
    if (window.location.pathname !== '/' && window.location.pathname !== '/login/') {
        // Verificar autenticación periódicamente
        setInterval(checkAuthentication, 30000); // Cada 30 segundos
        
        // Verificar al cargar la página
        checkAuthentication();
        
        // Manejar eventos de navegación
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                // La página se cargó desde cache (botón atrás)
                checkAuthentication();
            }
        });
        
        // Prevenir cache con headers meta
        if (!$('meta[http-equiv="Cache-Control"]').length) {
            $('head').append('<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">');
            $('head').append('<meta http-equiv="Pragma" content="no-cache">');
            $('head').append('<meta http-equiv="Expires" content="0">');
        }
    }

    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    $('a[href*="#"]').on('click', function(e) {
        if (this.hash !== "") {
            e.preventDefault();
            var hash = this.hash;
            
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800);
        }
    });

    // Auto-hide alerts after 5 seconds
    $('.alert').each(function() {
        var alert = $(this);
        setTimeout(function() {
            alert.fadeOut('slow');
        }, 5000);
    });

    // Form validation enhancement
    $('.needs-validation').on('submit', function(e) {
        if (!this.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
        }
        $(this).addClass('was-validated');
    });

    // Loading state for buttons
    $('.btn-loading').on('click', function() {
        var btn = $(this);
        var originalText = btn.html();
        
        btn.html('<i class="fas fa-spinner fa-spin me-2"></i>Cargando...');
        btn.prop('disabled', true);
        
        // Restore button after 3 seconds (adjust as needed)
        setTimeout(function() {
            btn.html(originalText);
            btn.prop('disabled', false);
        }, 3000);
    });

    // Data tables enhancement
    if ($.fn.DataTable) {
        $('.data-table').DataTable({
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json"
            },
            "responsive": true,
            "pageLength": 25,
            "order": [[ 0, "desc" ]]
        });
    }

    // Search functionality
    $('#searchInput').on('keyup', function() {
        var value = $(this).val().toLowerCase();
        $('.searchable').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    // Confirmation modals
    $('.confirm-delete').on('click', function(e) {
        e.preventDefault();
        var url = $(this).attr('href');
        var message = $(this).data('message') || '¿Estás seguro de que quieres eliminar este elemento?';
        
        if (confirm(message)) {
            window.location.href = url;
        }
    });

    // Number formatting
    $('.format-number').each(function() {
        var number = parseInt($(this).text());
        if (!isNaN(number)) {
            $(this).text(number.toLocaleString('es-CO'));
        }
    });

    // Currency formatting
    $('.format-currency').each(function() {
        var amount = parseFloat($(this).text());
        if (!isNaN(amount)) {
            $(this).text('$' + amount.toLocaleString('es-CO', {
                minimumFractionDigits: 0,
                maximumFractionDigits: 0
            }));
        }
    });

    // Date formatting
    $('.format-date').each(function() {
        var dateStr = $(this).text();
        var date = new Date(dateStr);
        if (!isNaN(date.getTime())) {
            $(this).text(date.toLocaleDateString('es-CO'));
        }
    });

    // Toggle sidebar (if implemented)
    $('#sidebarToggle').on('click', function() {
        $('.sidebar').toggleClass('collapsed');
        $('.main-content').toggleClass('expanded');
    });

    // Back to top button
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    });

    $('.back-to-top').on('click', function() {
        $('html, body').animate({scrollTop: 0}, 600);
        return false;
    });

    // Print functionality
    $('.print-btn').on('click', function() {
        window.print();
    });

    // Export functionality placeholder
    $('.export-btn').on('click', function() {
        var format = $(this).data('format');
        alert('Exportando en formato: ' + format.toUpperCase());
        // Implement actual export functionality here
    });

    // Dynamic form fields
    $('.add-field').on('click', function() {
        var template = $(this).data('template');
        var container = $(this).data('container');
        
        if (template && container) {
            $(container).append($(template).html());
        }
    });

    $('.remove-field').on('click', function() {
        $(this).closest('.dynamic-field').remove();
    });

    // Real-time search
    $('.real-time-search').on('input', function() {
        var query = $(this).val();
        var target = $(this).data('target');
        
        if (query.length >= 3) {
            // Implement AJAX search here
            console.log('Searching for: ' + query);
        } else {
            $(target).empty();
        }
    });

    // Theme switcher (if implemented)
    $('.theme-switcher').on('click', function() {
        var theme = $(this).data('theme');
        $('body').attr('data-theme', theme);
        localStorage.setItem('theme', theme);
    });

    // Load saved theme
    var savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        $('body').attr('data-theme', savedTheme);
    }
});

// Utility functions
function showNotification(message, type = 'info') {
    var alertClass = 'alert-' + type;
    var notification = $('<div class="alert ' + alertClass + ' alert-dismissible fade show" role="alert">' +
        message +
        '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>' +
        '</div>');
    
    $('.notifications-container').prepend(notification);
    
    setTimeout(function() {
        notification.fadeOut();
    }, 5000);
}

function formatPhoneNumber(phone) {
    // Format Colombian phone numbers
    var cleaned = phone.replace(/\D/g, '');
    var match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
        return match[1] + '-' + match[2] + '-' + match[3];
    }
    return phone;
}

function validateEmail(email) {
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateColombianID(id) {
    // Basic Colombian ID validation
    var cleaned = id.replace(/\D/g, '');
    return cleaned.length >= 6 && cleaned.length <= 10;
}

// Export functions for global use
window.CRM = {
    showNotification: showNotification,
    formatPhoneNumber: formatPhoneNumber,
    validateEmail: validateEmail,
    validateColombianID: validateColombianID
};

// Función para verificar autenticación
function checkAuthentication() {
    $.ajax({
        url: '/check-auth/',
        type: 'GET',
        timeout: 5000,
        success: function(response) {
            if (!response.authenticated) {
                window.location.href = '/login/';
            }
        },
        error: function() {
            // En caso de error, redirigir al login para mayor seguridad
            window.location.href = '/login/';
        }
    });
}