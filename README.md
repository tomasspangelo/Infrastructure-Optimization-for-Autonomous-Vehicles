# Infrastructure Optimization for Autonomous Vehicles
## 1 File structure
The file structure of this project can be visualized in the following tree:
```
Infrastructure-Optimization-for-Autonomous-Vehicles
│   README.md
│   README.pdf
│   report.pdf    
│   requirements.txt
│
└───Mosel
│   │   AutonomaxData.txt
│   │   autonomax.mos
│   │	out.txt
│   |	plot.py
│   |	run_plot.py
|   |	run_subset_script.py
|   |	subset_script.py
|   |	subsets.txt
|
└───Runs
    │   cycle3.txt
    │   cycle4scen2.txt
    │	...
```

The folder `/Mosel` contains everything that is related to the implementation of the mathematical model, which includes the Mosel implementation, supplementary python scripts, data files, output files etc. The folder `/Runs` contains the history of saved output files (same format as out.txt) from runs with different parameter settings which includes all of the information that is relevant to the solution for the given run. If the filename contains "no" (not optimal) it is not solved to optimality, and if scen[number] is not specified in the filename then Scenario=1. 

## 2 How to run the model locally

 1. Open the `autonomax.mos` file in Xpress Workbench (or any other IVE/IDE that let's you run mosel code).
 2. Before you run the model in Xpress, you need to make sure that you have the latest version of the programming language [Python](https://www.python.org/) installed on your computer.
 3. The python scripts that will be directly called from `autonomax.mos` in Xpress have some dependencies that you need to install. These requirements can be found in the file  `requirements.txt`. Use your favorite package manager/installer to install the requirements, we recommend using [pip](https://pypi.org/project/pip/). To install the requirements, run the following command **in the root folder of the project** (where `requirements.txt` is located):
	 
	 `pip install -r requirements.txt`
4. Now you should be all set. Run the model by clicking `Run`.  Relevant information about the solution will be printed to the console, as well as written to `/Mosel/out.txt`.  The python script `plot.py` will use this output file to display a graphical network plot of the solution.

### 2.1 If you get an error and cannot run the model properly 

Do not worry! The Xpress-package `python3` does not work for all computers and operating systems. Here we will explain how to work around this.

**Short:**

 1. Remove the lines `pyrun("run_subset_script.py");` and `pyrun("run_plot.py");` in `autonomax.mos` by either making them comments (!) or simply deleting them.
 2. Run `subset_script.py` in the `/Mosel` folder using your favorite Python IDE or terminal command to generate the subsets used for the subtour elimination constraints to `subsets.txt`. Make sure all parameters in the Mosel parameter environment is set to the values you want to use before you run the script.
 3. Run the Mosel model in Xpress.
 4. Optional: Once the model is finished run `plot.py` in the `/Mosel`folder using your favorite Python IDE or terminal command. This is not necessary, as it will only plot the solution and does not affect the results.

**Detailed:**

In `autonomax.mos`, the python script `run_subsets_script.py` is called using the `pyrun()` command:

![enter image description here](https://i.ibb.co/KNX7886/Skjermbilde-2021-03-30-kl-17-08-12.png)			

This short script will in turn run a command on your computer in order to properly run `subset_script.py` (which generates the subsets and write them to `/Mosel/subsets.txt`):

![enter image description here](https://i.ibb.co/8sLSdzZ/Skjermbilde-2021-03-30-kl-17-15-41.png)

Similarly, after Xpress is finished solving the problem, the python script `run_plot.py`  is run using  `pyrun()`  in order to properly run `plot.py` (which plots the solution graphically):

![enter image description here](https://i.ibb.co/smBjXPH/Skjermbilde-2021-03-30-kl-17-22-08.png)


Your operating system has either problems with the run-scripts that call the desired scripts using terminal commands, or there is a problem with the `python3` Xpress-package.
