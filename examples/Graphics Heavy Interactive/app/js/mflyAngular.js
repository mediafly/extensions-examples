'use strict';

var HOSTNAME = window.location.origin.indexOf('localhost') > 0 ? "http://localhost:8000/" : "mfly://";

function mflyDataInit(obj) {
    var $scope = angular.element('body').scope();
    $scope.$broadcast('Mediafly.mflyDataInit', obj);
    return "{ 'mflyInitVersion': '4', 'mflyWideScreenSupport': true }";
}

function mflyInit(obj) {
    var $scope = angular.element('body').scope();
    $scope.$apply(function() {
        $scope.$broadcast('Mediafly.mflyInit', obj);
    });
}

function mflyResume() {
    var $scope = angular.element('body').scope();
    $scope.$apply(function() {
        $scope.$broadcast('Mediafly.mflyResume');
    });
}

function mflySync(obj) {
    var $scope = angular.element('body').scope();
    $scope.$apply(function() {
        $scope.$broadcast('Mediafly.mflySync', obj);
    });
}




/* Services */
angular.module('Mediafly.services', []).
    factory('MflyMetadataService', ['$http', function ($http) {
        return {
            getFolder: function (key) {
                console.log("MflyMetadataService.getFolder: key=",key);
                return $http({
                    method: 'GET',
                    url: HOSTNAME + 'data/folder/' + key
                }).success(function (data, status, headers, config) {
                    // resolve the promise as the data
                    return data;
                }).error(function (data, status, headers, config) {
                    console.log('MflyMetadataService.getFolder ERROR: what should I do now? data=' + data + ' status=' + status);
                });
            },

            getItem: function (key) {
                console.log("MflyMetadataService.getItem: key=", key);
                return $http({
                    method: 'GET',
                    url: HOSTNAME + 'data/item/' + key
                }).success(function (data, status, headers, config) {
                    // resolve the promise as the data
                    return data;
                }).error(function (data, status, headers, config) {
                    console.log('MflyMetadataService.getItem ERROR: what should I do now? data=' + data + ' status=' + status);
                });
            }
        };
    }]).
    factory('MflyDataService', ['$http', function ($http) {
        return {
            saveState: function (key, value) {
                //return the promise directly.
                // TODO: Using Angular.JS's $http with mfly:// calls is not working. Use jQuery AJAX temporarily.
/*
                return $http({
                    method: 'GET',
                    url: 'mfly://data/info/' + key,
                    data: 'value=' + encodeURIComponent(value) + '&method=PUT',
                    dataType: 'text',
                    headers: {
                        "Content-Type": "text/plain; charset=utf-8"
                    }
                }).success(function (data, status, headers, config) {
                        // resolve the promise as the data
                        return data;
                    }).error(function (data, status, headers, config) {
                        console.log('MflyDataService.saveState ERROR: what should I do now? data=' + data + ' status=' + status);
                    });
*/

                return $.ajax({
                    type: "GET",
                    url: HOSTNAME + "data/info/" + key,
                    contentType: "text/plain; charset=utf-8",
                    data: "value=" + encodeURIComponent(value) + "&method=PUT",
                    dataType: "text"
                }).success(function (result, status, xhr) {
                    return result;
                }).error(function (xhr, status, error) {
                    console.log('MflyDataService.saveState ERROR: what should I do now? status=' + status + ' error=' + error);
                });
            },

            getState: function (key) {
                //return the promise directly.
                return $http({
                    method: 'GET',
                    url: HOSTNAME + 'data/info/' + key
                }).success(function (data, status, headers, config) {
                        // resolve the promise as the data
                        return data;
                    }).error(function (data, status, headers, config) {
                        console.log('MflyDataService.getState ERROR: what should I do now? data=' + data + ' status=' + status);
                    });
            }
        };
    }]);
