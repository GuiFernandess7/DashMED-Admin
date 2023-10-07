import React from 'react'
import {Box, Typography, useTheme} from "@mui/material";
import {DataGrid, GridToolbar, GridActionsCellItem} from '@mui/x-data-grid'
import { tokens } from '../../theme'
import MedicalInformationOutlinedIcon from '@mui/icons-material/MedicalInformationOutlined';
import DeleteIcon from '@mui/icons-material/Delete'
import Header from '../../components/Header';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import Collapse from '@mui/material/Collapse';

//import { GridRenderCellParams } from '@mui/x-data-grid';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';

import { useState } from 'react'

import useSWR from 'swr'

import { 
  getDoctors,
  doctorsEndpoint as cacheKey
} from '../../api/doctors';

const Doctors = () => {
  const [clickedIndex, setClickedIndex] = useState(-1)
  const theme = useTheme()
  const colors = tokens(theme.palette.mode);

  const detailStyles={
    borderTop: "2px solid",
    borderTopColor: "primary.main",
    pt: 2
  }

  const deleteDoctor = () => {
    console.log("Test")
  }

  const columns = [
    {
      field: "id", 
      headerName: "ID",
    },
    {
      field: "name", 
      headerName: "Name", 
      cellClassName: "name-column--cell",
      flex: 1,
    },
    {
      field: "age",
      headerName: "Age",
      type: "number",
    },
    {
      field: "email",
      headerName: "Email",
      flex: 1,
    },
    {
      field: "specialty",
      headerName: "Especialidade",
      renderCell: ({row: {specialty}}) => {
        return (
          <Box
            width="60%"
            m="0 auto"
            p="5px 45px"  
            display="flex"
            justifyContent="center"
            backgroundColor= {colors.greenAccent[800]}
            borderRadius="4px"
          >
            {<MedicalInformationOutlinedIcon/>}
            <Typography color={colors.grey[100]} sx={{ ml: "5px"}}>
              {specialty}
            </Typography>
          </Box>
        )
      }
    },
    {
      field: 'delete',
      headerName: "Delete",
      type: 'actions',
      width: 80,
      flex: 1,
      getActions: (params) => [
        <GridActionsCellItem
          icon={<DeleteIcon/>}
          label="Delete"
          onClick={deleteDoctor}
        />
      ]
    },
    {
      field: 'options',
      headerName: "Detail",
      type: 'actions',
      width: 80,
      flex: 1,
      renderCell: (cellValues => {
        return (
        <IconButton onClick={()=>
        {clickedIndex === cellValues.value ? setClickedIndex(-1) : setClickedIndex(cellValues.value)}}>
          {cellValues.value === clickedIndex ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon/>}
        </IconButton>)
      })
    },
  ]

  const {
    isLoading, 
    error, 
    data: doctors,
    mutate,
  } = useSWR(cacheKey, getDoctors, {
    onSuccess: data => data.sort((a, b) => b.id - a.id) // reverse the order of the ID of data
  })

  return (
    <Box m="20px">
          <Box display="flex" justifyContent="space-between" alignItems="center">
            <Header title="MÉDICOS" subtitle="Acesso a lista de médicos"/>
            <Button variant="contained" color="primary">
              Adicionar Médico
            </Button>
          </Box>
          <Box m="10px 0 0 0" height="68vh" sx={{
            "& .MuiDataGrid-root": {
              border: "none"
            },
            "&. MuiDataGrid-root": {
              borderBottom: "none"
            },
            "& .name-column--cell": {
              color: colors.greenAccent[300]
            },
            "& .MuiDataGrid-columnHeaders": {
              backgroundColor: colors.blueAccent[700],
              borderBottom: "none"
            },
            "$ .MuiDataGrid-virtualScroller": {
              backgroundColor: colors.primary[400]
            },
            "& .MuiDataGrid-footerContainer": {
              borderTop: "none",
              backgroundColor: colors.blueAccent[700]
            },
            "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
              color: `${colors.grey[100]} !important`
            }
          }}>
            <DataGrid rows={doctors || []} columns={columns} components={{Toolbar: GridToolbar}}/>
          </Box>
    </Box>
  )
}

export default Doctors;