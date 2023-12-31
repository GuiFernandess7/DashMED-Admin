import React from 'react'
import {Box, Typography, useTheme} from "@mui/material";
import {DataGrid, GridToolbar, GridActionsCellItem} from '@mui/x-data-grid'
import { tokens } from '../../theme'
import Button from '@mui/material/Button';
import PriorityHighIcon from '@mui/icons-material/PriorityHigh';
import LowPriorityIcon from '@mui/icons-material/LowPriority';
import DeleteIcon from '@mui/icons-material/Delete'
import Header from '../../components/Header';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';


import { useState } from 'react'

import useSWR from 'swr'

import { 
  getPatients,
  patientsEndpoint as cacheKey
} from '../../api/patients';

const Patients = () => {
  const [patient, setPatient] = useState([])
  const theme = useTheme()
  const colors = tokens(theme.palette.mode);

  const deletePatient = () => {
    console.log("test")
  }

  const columns = [
    {field: "id", headerName: "ID", flex: 0.5},
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
      flex: 1
    },
    {
      field: "priority",
      headerName: "Prioridade",
      renderCell: ({row: {priority}}) => {
        return (
          <Box
            width="60%"
            m="0 auto"
            p="5px 43px"  
            display="flex"
            justifyContent="center"
            backgroundColor={
              priority === "low"
                ? colors.greenAccent[600]
                : colors.greenAccent[700]
            }
            borderRadius="4px"
          >
            {priority === "high" && <PriorityHighIcon/>}
            {priority === "low" && <LowPriorityIcon/>}
            {priority === "medium" && <LowPriorityIcon/>}
            <Typography color={colors.grey[100]} sx={{ ml: "5px"}}>
              {priority}
            </Typography>
          </Box>
        )
      }
    },
    {
      field: 'action',
      headerName: "Options",
      type: 'actions',
      width: 80,
      flex: 1,
      getActions: (params) => [
        <GridActionsCellItem
          icon={<DeleteIcon/>}
          label="Delete"
          onClick={deletePatient}
        />
      ]
    }
    
  ]

  const {
    isLoading, 
    error, 
    data: patients,
    mutate,
  } = useSWR(cacheKey, getPatients, {
    onSuccess: data => data.sort((a, b) => b.id - a.id) // reverse the order of the ID of data
  })

  return (
    <Box m="20px">
          <Box display="flex" justifyContent="space-between" alignItems="center">
            <Header title="PACIENTES" subtitle="Acesso a lista de pacientes" />
            <Button variant="contained" color="primary">
              Adicionar Paciente
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
            <DataGrid rows={patients || []} columns={columns} components={{Toolbar: GridToolbar}} />
          </Box>
    </Box>
  )
}

export default Patients;