(function(){
    angular.module('App', [])
        .config(function($interpolateProvider){
            $interpolateProvider.startSymbol('@@').endSymbol('@@');
});

}());

(function(){
    function MainCtrl($scope, $http){
        this.$http = $http;
        $scope.title = 'First Page';
        this.getBlats()

    }

    MainCtrl.prototype.getBlats = function (){

        this.$http.get('/api/blats/')
            .success(function(res){

                debugger

            })

    }

    angular.module('App')
        .controller('MainCtrl', MainCtrl)
}());