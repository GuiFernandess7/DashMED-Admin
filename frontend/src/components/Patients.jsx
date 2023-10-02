import React from 'react'
import {Box} from "@mui/material";
import Header from "./Header"
import toast, { Toaster } from 'react-hot-toast'
//import { FontAwesomeIcon } from "@fontawesome/react-fontawesome"
//import { faTrash, faUpload } from "@fontawesome/free-solid-svg-icons"
import { useState } from 'react'

import useSWR from 'swr'

import { 
  getPatients,
  patientsEndpoint as cacheKey
} from '../api/patients';

const Patients = () => {
  const [patient, setPatient] = useState([])

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
            <Header title="PACIENTES" subtitle="Acesso a lista de pacientes"/>
        </Box>
        <div>{patients.map((patient)=> (
          <div className='patient' key={patient.id}>
            <h2>{patient.name} - {patient.id}</h2>
          </div>
        ))}</div>
    </Box>
  )
}

export default Patients;