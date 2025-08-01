# c'est moi
 * comment vas t-u
bash```
sudo apt install markdown discount
vi README.md #write something
mkd2html "README.md" "readme"


```
* do
````
sudo apt install markdown discount
vi README.md #write something
mkd2html "README.md" "readme"
python -m venv tutorial-env
source tutorial-env/bin/activate
flask run --host=0.0.0.0
#for ruby
irb
Kernel.at_exit {
  File.open("irb.log", "w") do |f|
    f << Readline::HISTORY.to_a.join("\n")
  end
}

````
* When you exit IRB the input history will be saved to irb.log in your current working directory. It will also work if you’ve already run some commands and then paste the above block.
* Here is a quick solution: Create .irbrc file in your home directory and paste following line into it: IRB.conf[:SAVE_HISTORY] = 1000
- for python3
````
import readline
readline.write_history_file('python_history.txt')
````
