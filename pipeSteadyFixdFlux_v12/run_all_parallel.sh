#!/bin/bash

foamCleanCase
rm -r 0
cp -r 0_orig 0

blockMesh | tee log.blockMesh
checkMesh | tee log.checkMesh

decomposePar

mpirun -np 4 foamRun -parallel | tee log.solver

reconstructPar -latestTime

foamLog log.solver

rm -r processor* 
