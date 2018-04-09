'use strict';

/* Controllers */

var CONSTANTS = {
    'TV_FOLDER': 'fb568c0d0873472690cfe8ba857943a0product131094',
    'MOVIE_FOLDER': 'fb568c0d0873472690cfe8ba857943a0product131112'
};

angular.module('myApp.controllers', []).
    controller('TVCtrl', ['$scope', 'MflyDataService', 'MflyMetadataService', function ($scope, MflyDataService, MflyMetadataService) {
        $scope.$on('Mediafly.mflySync', function(obj) {
            console.log('Mediafly.mflySync: obj=', obj);
            for (var o in obj) {
                if (o.id == CONSTANTS.TV_FOLDER) {
                    console.log('TV FOLDER FOUND; resynching')
                    $scope.resyncFolders();
                }
            }
        }),

        $scope.resyncFolders = function() {
            MflyMetadataService.getFolder(CONSTANTS['TV_FOLDER'])
                .success(function(data) {
                    $scope.titles = data;
                }).error(function(data, status) {
                    // TODO how to handle errors?
                });
        },

        $scope.resyncFolders();

    }]).
    controller('MoviesCtrl', ['$scope', 'MflyDataService', 'MflyMetadataService', function ($scope, MflyDataService, MflyMetadataService) {
        $scope.$on('Mediafly.mflySync', function(obj) {
            console.log('Mediafly.mflySync: obj=', obj);
            for (var o in obj) {
                if (o.id == CONSTANTS.MOVIE_FOLDER) {
                    console.log('MOVIE FOLDER FOUND; resynching')
                    $scope.resyncFolders();
                }
            }
        }),

        $scope.resyncFolders = function() {
            MflyMetadataService.getFolder(CONSTANTS['MOVIE_FOLDER'])
                .success(function(data) {
                    $scope.titles = data;
                }).error(function(data, status) {
                    // TODO how to handle errors?
                });
        },

        $scope.resyncFolders();
    }]).
    controller('LargeThumbnailCtrl', ['$scope', 'MflyDataService', 'MflyMetadataService', function ($scope, MflyDataService, MflyMetadataService) {
        MflyMetadataService.getItem('fb568c0d0873472690cfe8ba857943a0product153299')
            .success(function(folder) {
                $('#largethumbnail').attr('src', folder['thumbnailUrl']);
            });
    }]);
;
