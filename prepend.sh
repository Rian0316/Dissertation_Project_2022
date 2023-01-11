#!/bin/bash
file=$1
nl -s " @@ " $file | tee $file-no
