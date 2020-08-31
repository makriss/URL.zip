

app.controller('zipperCtrl', ['$scope', '$http', '$timeout', function(scope, $http, $timeout){
    window.scope = scope;
    scope.minifiedUrlsList = [];

    scope.minifyUrl = function(url){
        if (!url){ // if url input is blank, show error msg and return
            showErrorMessage('blank');
            return;
        }
        console.log(url);

        url = fetchMinifiedUrl(url);


    }

    function fetchMinifiedUrl(url){
        $http.post('/zip/', {'url': url})
            .then(function(result){
                console.info(result.data);
                if (!result.data.minified_url)
                    showErrorMessage(result.data.value, result.data.msg)
                else{
                    scope.minifiedUrlsList.push(result.data);
                    scope.url_string = "";
                    }
            },
            function(result){
                console.error(result);
            } )
    }


    function showErrorMessage(type, msg = null){
        switch(type){
            case 'blank': scope.errorMessage = msg || "Please provide a url";
                                break;
            case 'invalid': scope.errorMessage = msg || "Please enter a valid url";
                                break;
        }
    }

    scope.copyUrl = function(url_object){
        navigator.clipboard.writeText(url_object.minified_url)
          .then(() => {
                url_object.btnText = "Copied!";
                url_object.copied = true;
                scope.$apply();
//            inputEl.value = '';
//            if (writeBtn.innerText !== 'Copied!') {
//              const originalText = writeBtn.innerText;
//              writeBtn.innerText = 'Copied!';
              $timeout(() => {
                url_object.btnText = "";
                url_object.copied = false;
                console.log("Over");
              }, 1500);
//            }
          })
      .catch(err => {
        console.log('Something went wrong', err);
      })
    }

}])
