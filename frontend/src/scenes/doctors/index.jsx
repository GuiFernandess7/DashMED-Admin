import React from 'react'
import {Box, Typography, useTheme} from "@mui/material";
import {DataGrid, GridToolbar} from '@mui/x-data-grid'
import { tokens } from '../../theme'
import PriorityHighIcon from '@mui/icons-material/PriorityHigh';
import LowPriorityIcon from '@mui/icons-material/LowPriority';
import MedicalInformationOutlinedIcon from '@mui/icons-material/MedicalInformationOutlined';
import Header from '../../components/Header';

import { useState } from 'react'

import useSWR from 'swr'

import { 
  getDoctors,
  doctorsEndpoint as cacheKey
} from '../../api/doctors';

const Doctors = () => {
  const theme = useTheme()
  const colors = tokens(theme.palette.mode);

  const columns = [
    {field: "id", headerName: "ID"},
    {
      field: "name", 
      headerName: "Name", 
      cellClassName: "name-column--cell",
      flex: 1
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
      field: "specialty",
      headerName: "Especialidade",
      renderCell: ({row: {specialty}}) => {
        return (
          <Box
            width="60%"
            m="0 auto"
            p="5px 43px"  
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
    }
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
          <Header title="MÉDICOS" subtitle="Acesso a lista de médicos"/>
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
            }
          }}>
            <DataGrid rows={doctors || []} columns={columns} />
          </Box>
    </Box>
  )
}

export default Doctors;