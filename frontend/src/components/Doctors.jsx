import React from 'react'
import {Box} from '@mui/material'
import Header from "./Header"

const Doctors = () => {
  return (
    <Box m="20px">
        <Box display="flex" justifyContent="space-between" alignItems="center">
            <Header title="MÉDICOS" subtitle="Acesso a lista de médicos"/>
        </Box>
    </Box>
  )
}

export default Doctors