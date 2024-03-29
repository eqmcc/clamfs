dnl Copyright (C) 1999-2005 Open Source Telecom Corporation.
dnl Copyright (C) 2006-2008 David Sugar, Tycho Softworks. 
dnl  
dnl This program is free software; you can redistribute it and/or modify
dnl it under the terms of the GNU General Public License as published by
dnl the Free Software Foundation; either version 2 of the License, or
dnl (at your option) any later version.
dnl 
dnl This program is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl GNU General Public License for more details.
dnl 
dnl You should have received a copy of the GNU General Public License
dnl along with this program; if not, write to the Free Software 
dnl Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
dnl 
dnl As a special exception to the GNU General Public License, if you 
dnl distribute this file as part of a program that contains a configuration 
dnl script generated by Autoconf, you may include it under the same 
dnl distribution terms that you use for the rest of that program.

AC_DEFUN([OST_CC_GETOPT],[
	ost_cv_libgetopt_long=false
	GETOPT_LIBS=""
	LIBGETOPTOBJS=""
	AC_REQUIRE([OST_SYS_POSIX])
	AC_CHECK_FUNCS(getopt,
		[AC_DEFINE(HAVE_GETOPT, [1], [have getopt header])],[
		AC_CHECK_LIB(m, getopt,
			[AC_DEFINE(HAVE_GETOPT, [1])
		 	GETOPT_LIBS="-lm"])
		])
	AC_CHECK_HEADERS(getopt.h)
	AC_CHECK_LIB(gnugetopt, getopt_long,
		[AC_DEFINE(HAVE_GETOPT_LONG, [1], [have gnugetopt lib])
		 GETOPT_LIBS="-lgnugetopt $GETOPT_LIBS"
		 LIBS="$LIBS -lgnugetopt"],
		[AC_CHECK_FUNCS(getopt_long,
			[AC_DEFINE(HAVE_GETOPT_LONG, [1])],
			[LIBGETOPTOBJS="getopt.c getopt1.c"])]
	)
	AC_SUBST(GETOPT_LIBS)
	AC_SUBST(LIBGETOPTOBJS)
])

