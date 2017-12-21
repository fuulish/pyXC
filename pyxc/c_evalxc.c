#include <stdlib.h>
#include <stdio.h>
#include <xc.h>

long int c_xc_energy_density( double * exc, double * rho, double * sigma, long int len, long int * func_id, long int nfunc )
{
  int i, k, vmajor, vminor;

  xc_func_type func;
  double *tmpexc;

  tmpexc = ( double * ) malloc ( len * sizeof ( double ) );

  xc_version(&vmajor, &vminor);
  printf("Libxc version: %d.%d\n", vmajor, vminor);

  for ( i=0; i<nfunc; i++ ) {

    // need to initialize the functional
    if(xc_func_init(&func, func_id[i], XC_UNPOLARIZED) != 0){
      fprintf(stderr, "Functional '%ld' not found\n", func_id[0]);
      free( tmpexc );
      return 1;
    }

    switch(func.info->family)
    {
      case XC_FAMILY_LDA:
        xc_lda_exc ( &func, len, rho, tmpexc );
        // printf("HELLO\n");
        break;
      case XC_FAMILY_GGA:
      case XC_FAMILY_HYB_GGA:
        xc_gga_exc ( &func, len, rho, sigma, tmpexc );
        break;
    }

    for( k=0; k<len; ++k )
      exc[k] += tmpexc[k];

    // and need to let the functional go
    xc_func_end(&func);

  }

  free( tmpexc );

  return 0;

}
