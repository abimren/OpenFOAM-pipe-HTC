#!/bin/bash

foamCleanTutorials
rm -r 0 logs
cp -r 0_orig 0

blockMesh | tee log.blockMesh
checkMesh | tee log.checkMesh

decomposePar

mpirun -np 4 rhoSimpleFoam -parallel | tee log.solver

reconstructPar -latestTime

foamLog log.solver

rm -r processor* 
