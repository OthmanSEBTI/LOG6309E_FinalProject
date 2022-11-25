#! /usr/bin/bash

cd Git\ repos

declare -a Listegit=(
"ShareX/ShareX" "NancyFx/Nancy" "electron/electron" "bitcoin/bitcoin" "BVLC/caffe" "metabase/metabase" 
"technomancy/leiningen" "LightTable/LightTable" "Atom/atom" "jashkenas/coffeescript" "postcss/autoprefixer"
"neovim/neovim" "junegunn/vim-plug" "mhinz/vim-galore" "Microsoft/vscode" "angular/angular" "Microsoft/TypeScript"
 "soulmachine/leetcode" "adambard/learnxinyminutes-docs" "cplusplus/draft" "qinwf/awesome-R" 
 "rstudio/shiny" "twitter/AnomalyDetection" "rails/rails" "jekyll/jekyll" "discourse/discourse" "jwilm/alacritty" 
 "redox-os/redox" "BurntSushi/ripgrep" "scala/scala" "akka/akka" "twitter/finagle""tldr-pages/tldr" 
 "Tj/git-extras" "jwilder/nginx-proxy""Alamofire/Alamofire" "vsouza/awesome-ios" "SwiftyJSON/SwiftyJSON"
  "getlantern/lantern" "avelino/awesome-go" "ethereum/go-ethereum"  
 "koalaman/shellcheck" "jgm/pandoc" "purescript/purescript"
 "necolas/normalize.css" "google/material-design-lite" "google/web-starter-kit"
 "ReactiveX/RxJava" "iluwatar/java-design-patterns" "square/retrofit"   
 "FreeCodeCamp/freecodecamp" "facebook/react" "airbnb/javascript"  
 "syl20bnr/spacemacs" "emacs-tw/awesome-emacs" "purcell/emacs.d"  
 "cmusatyalab/openface" "martanne/vis" "luvit/luvit"  
 "ReactiveCocoa/ReactiveCocoa" "dkhamsing/open-source-ios-apps" "Realm/realm-cocoa"  
 "major/MySQLTuner-perl" "jlord/git-it-electron" "sjdy521/Mojo-Webqq"
 "bcit-ci/CodeIgniter" "symfony/symfony" "composer/composer"  
 "pester/Pester"  
 "vinta/awesome-python nvbn/thefuck" "scikit-learn/scikit-learn"
 "twbs/bootstrap" "google/material-design-icons" "jgthms/bulma"  "elixir-lang/elixir" "phoenixframework/phoenix" "h4cc/awesome-elixir"  
"erlang/otp" "rabbitmq/rabbitmq-server" "processone/ejabberd")


for ((i=0;i<78;i=i+1)) ; do

    git clone "https://github.com/${Listegit[i]}.git"
    
done