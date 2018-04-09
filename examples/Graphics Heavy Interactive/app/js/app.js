'use strict';


$(document).ready(function() {
  // Handle events fired within JavaScript/jQuery, and pass them into Angular.
  $('#launchModal').on('hidden.bs.modal', function () {
    angular.element('body').scope().launchModalClosed();
  });
});


// Declare app level module which depends on filters, and services
angular.
    module('myApp', ['myApp.controllers', 'Mediafly.services']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/tv', {templateUrl: 'partials/grid_tallimages.html', controller: 'TVCtrl'});
        $routeProvider.when('/movies', {templateUrl: 'partials/grid_tallimages.html', controller: 'MoviesCtrl'});
        $routeProvider.when('/largethumbnail', {templateUrl: 'partials/largethumbnail.html', controller: 'LargeThumbnailCtrl'});
        $routeProvider.otherwise({redirectTo: '/tv'});
    }]);
