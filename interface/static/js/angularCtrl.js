
app.controller('zipperCtrl', ['$scope', '$http', '$timeout', function(scope, $http, $timeout){
    window.scope = scope;
    scope.minifiedUrlsList = [];
    const URL_VERBOSE_LIMIT = 20,
            COPIED_DISPLAY_TIME = 1500;

// Called when user clicks on 'zip it' button
    scope.minifyUrl = function(url){
        if (!url){ // if url input is blank, show error msg and return
            showErrorMessage('blank');
            return;
        }
        url = fetchMinifiedUrl(url);
    }

// Calls rest api and retrieves minified url
    function fetchMinifiedUrl(url){
        $http.post('/zip/', {'url': url})
            .then(function(result){
                console.info(result.data);
                if (!result.data.minified_url)  // error message is displayed to user
                    showErrorMessage(result.data.value, result.data.msg)
                else{ // Url object is pushed to user and all minfied urls are displayed as a list
                    scope.minifiedUrlsList.push(result.data);
                    scope.url_string = "";  // Input field is set empty
                    }
            },
            function(result){
                console.error(result);
            } )
    }

// Selects and displays error message based on the type of error
    function showErrorMessage(type, msg = null){
        switch(type){
            case 'blank': scope.errorMessage = msg || "Please provide a url";
                                break;
            case 'invalid': scope.errorMessage = msg || "Please enter a valid url";
                                break;
            default: scope.errorMessage = msg || "Encountered an error. Please try again";
                        break;
        }
    }

// Called on clicking the 'copy' button, and copies the minified url to clipboard
// It will change the text of button to "Copied" and initiate a timer to revert back the name
    scope.copyUrl = function(url_object){
        navigator.clipboard.writeText(url_object.minified_url)
          .then(() => {
                url_object.btnText = "Copied!";
                url_object.copied = true;
                scope.$apply();
                $timeout(() => {
                    url_object.btnText = "";
                    url_object.copied = false;
                }, COPIED_DISPLAY_TIME);
//            }
          })
      .catch(err => {
        console.error('Something went wrong', err);
      })
    }

// Long urls will be truncated above the mentioned limit and displayed with '...' in the end
    scope.trimVerboseUrl = function(){
        if (this.url.length< URL_VERBOSE_LIMIT)
            return this.url;
        else
            return this.url.substring(0, URL_VERBOSE_LIMIT) +  "...";
    }

}])
