/*** Copyright (c), The Regents of the University of California            ***
 *** For more information please refer to files in the COPYRIGHT directory ***/

#ifndef L3_FILE_GET_SINGLE_BUF_H__
#define L3_FILE_GET_SINGLE_BUF_H__

/* This is a Object File I/O call */

#include "rodsDef.h"
#include "rcConnect.h"

#if defined(RODS_SERVER)
#define RS_L3_FILE_GET_SINGLE_BUF rsL3FileGetSingleBuf
/* prototype for the server handler */
int
rsL3FileGetSingleBuf( rsComm_t *rsComm, int *l1descInx,
                      bytesBuf_t *dataObjOutBBuf );
#else
#define RS_L3_FILE_GET_SINGLE_BUF NULL
#endif

#ifdef __cplusplus
extern "C" {
#endif
int
rcL3FileGetSingleBuf( rcComm_t *conn, int l1descInx,
                      bytesBuf_t *dataObjOutBBuf );

#ifdef __cplusplus
}
#endif
#endif	// L3_FILE_GET_SINGLE_BUF_H__