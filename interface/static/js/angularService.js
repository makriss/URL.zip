app = angular.module('ZipperModule', [])

app.config(function($interpolateProvider, $httpProvider){
//    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.common['Content-Type'] = 'application/json';
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName=  "csrftoken";
    $httpProvider.defaults.xsrfHeaderName=  "X-CSRFToken";
});

app.directive('redAlert', function($timeout){
    return {
        restrict: 'E',
        scope: {
            msg: '='
        },
        template: '<div class="alert alert-danger" role="alert" ng-hide="!msg.length" ng-bind="msg"></div>',
        link: function(scope, elm, attr){
            window.ds = scope;
            scope.$watch('msg', function(newVal, oldVal){
                    $timeout(function(){
                        scope.msg = "";
                    }, 5000)
            })
        }

    }

})